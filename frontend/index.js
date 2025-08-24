function showError(id, message) {
  const el = document.getElementById(id);
  if (el) {
    el.innerText = message;
    el.classList.add("text-danger");
  } else {
    alert(message);
  }
}

//ASR
async function handleASR() {
  const outId = "asr-output-display";  // ID of the DOM element to show transcription
  const outEl = document.getElementById(outId);
  outEl.innerText = "⏳ Transcribing…";
 
  const fileInput = document.getElementById("asr-audio");
  if (!fileInput.files[0]) {
    showError(outId, "No file selected.");
    return;
  }

  const form = new FormData();
  form.append("file", fileInput.files[0]);

  try {
    const res = await fetch("/asr/", {
      method: "POST",
      body: form
    });

    if (!res.ok) {
      const errorText = await res.text();
      showError(outId, `Server Error: ${errorText}`);
      return;
    }

    const json = await res.json();

    // ✅ Log full ASR response
    console.log("✅ ASR raw JSON:", json);

    // 👇 Display transcription (support different possible key names)
    const transcription =
      json.transcription || json.original_text || json.text || "";

    if (!transcription) {
      showError(outId, "No transcription received.");
      return;
    }

    outEl.innerText = transcription;
    window.currentTranscriptionText = transcription;


    // Store transcript ID for later use (e.g. in translation step)
    const id =
      json.transcript_id ?? json.id ?? null;

    if (!id) {
      console.error("❌ Could not find transcript ID in ASR response!");
      alert("Internal error: no transcript_id returned from ASR");
      return;
    }

    window.currentTranscriptId = id;
    console.log("   → currentTranscriptId set to", window.currentTranscriptId);

  } catch (e) {
    console.error("Fetch error:", e.message);


  }
}

async function handleTranslate() {
    if (!window.currentTranscriptionText) {
        alert("Please transcribe an audio first.");
        return;
    }

    const langSelect = document.getElementById("translate-lang");
    const [srcLang, tgtLang] = langSelect.value.split("-");

    try {
        const response = await fetch("/translate/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: window.currentTranscriptionText,
                src_lang: srcLang,
                tgt_lang: tgtLang
            })
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("translate-output-display").innerText = result.translated_text;
        } else {
            alert("Translation Error: " + result.detail);
        }
    } catch (error) {
        alert("Translation Failed: " + error);
    }
}



// // Translation (Text to Text)
// async function handleTranslate() {
//     if (!window.currentTranscriptionText) {
//         alert("Please transcribe an audio first.");
//         return;
//     }

//     const langSelect = document.getElementById("translate-lang");
//     const langPair = langSelect.value.split("-");
//     const srcLang = langPair[0];
//     const tgtLang = langPair[1];

//     try {
//         const response = await fetch("/translate/", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({
//                 text: window.currentTranscriptionText,
//                 src_lang: srcLang,
//                 tgt_lang: tgtLang
//             })
//         });

//         const result = await response.json();

//         if (response.ok) {
//             document.getElementById("translate-output-display").innerText = result.translated_text;
//         } else {
//             alert("Translation Error: " + result.detail);
//         }
//     } catch (error) {
//         alert("Translation Failed: " + error);
//     }
// }


// ────── TTS handler ──────
async function handleTTS() {
  // 1) Grab the textarea
  const textEl = document.getElementById("tts-text");
  if (!textEl) {
    console.error("❌ No <textarea id='tts-text'> in the DOM");
    return;
  }

  // 2) Read its value
  const text = textEl.value;
  console.log("🚀 [1] text to send (raw):", text);
  console.log("🚀 [1] text to send (JSON):", JSON.stringify(text));

  if (!text) {
    showError("tts-audio", "Please type something first.");
    return;
  }

  // 3) Build FormData
  const formData = new FormData();
  formData.append("text", text);
  formData.append("lang", "en");

  try {
    // 4) POST to your FastAPI TTS endpoint
    console.log("🚀 [2] Sending POST to /tts/");
    const res = await fetch("/tts/", {
      method: "POST",
      body: formData
    });
    console.log("🚀 [3] Response:", res.status, res.statusText);

    if (!res.ok) {
      const errText = await res.text();
      console.error("🚨 Server error:", errText);
      showError("tts-audio", errText || res.statusText);
      return;
    }

    // 5) Read the MP3 blob
    const blob = await res.blob();
    console.log("🚀 [4] blob MIME type:", blob.type, "size:", blob.size);

    if (!blob.type.startsWith("audio/")) {
      const txt = await blob.text();
      console.warn("⚠️ Server returned non‑audio payload:", txt);
      showError("tts-audio", "Invalid audio received");
      return;
    }

    // 6) Hook it up to the <audio> element
    const audioURL = URL.createObjectURL(blob);
    const audioEl = document.getElementById("tts-audio");
    audioEl.src = audioURL;
    audioEl.load();

    // 7) Play!
    console.log("🚀 [5] Playing audio…");
    await audioEl.play();
    console.log("✅ Audio playback succeeded");

  } catch (err) {
    console.error("🛑 handleTTS caught:", err);
    showError("tts-audio", err.message);
  }
}



// 4) QA
async function handleQA() {
  const out = "qa-output";
  document.getElementById(out).innerText = "⏳ Thinking…";
  const question = document.getElementById("qa-question").value;
  try {
    const res = await fetch("/qa/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });
    if (!res.ok) {
      const err = await res.json();
      return showError(out, err.detail || JSON.stringify(err));
    }
    const { answer } = await res.json();
    document.getElementById(out).innerText = answer;
  } catch (e) {
    showError(out, e.message);
  }
}

// 5) Video
async function handleVideo() {
  const videoEl = document.getElementById("video-result");
  videoEl.src = "";
  const fileInput = document.getElementById("video-file");
  const lang      = document.getElementById("video-lang").value;
  if (!fileInput.files[0]) return alert("Please choose a video");

  const form = new FormData();
  form.append("file", fileInput.files[0]);
  form.append("target_lang", lang);

  try {
    const res = await fetch("/video/", { method: "POST", body: form });
    if (!res.ok) {
      const err = await res.json();
      return alert("Video error: " + (err.detail||JSON.stringify(err)));
    }
    const blob = await res.blob();
    videoEl.src = URL.createObjectURL(blob);
  } catch (e) {
    alert("Video processing error: " + e.message);
  }
}
