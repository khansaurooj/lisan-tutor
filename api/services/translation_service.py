from transformers import pipeline

def get_model_for_lang(src_lang: str, tgt_lang: str):
    # Normalize codes
    src = src_lang[:2].lower()
    tgt = tgt_lang[:2].lower()

    # Map language pairs to model names
    model_map = {
        ("en", "ur"): "Helsinki-NLP/opus-mt-en-ur",
        ("ur", "en"): "Helsinki-NLP/opus-mt-ur-en",
        ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
        ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
        ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
        ("es", "en"): "Helsinki-NLP/opus-mt-es-en"
    }

    model_name = model_map.get((src, tgt))
    if not model_name:
        raise ValueError(f"No model found for {src} → {tgt}")

    translator_pipeline = pipeline("translation", model=model_name)
    return translator_pipeline

def translate_text_pipeline(text: str, src_lang: str, tgt_lang: str) -> str:
    translator = get_model_for_lang(src_lang, tgt_lang)
    result = translator(text, max_length=512)
    return result[0]["translation_text"]