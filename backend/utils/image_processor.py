from transformers import BlipProcessor, BlipForConditionalGeneration
from backend.config.settings import settings
from PIL import Image
from typing import Any

class ImageProcessor:
    """Processa imagens e gera descrições usando o modelo BLIP.

    A classe guarda o processador e o modelo em memória para evitar recarregar
    tudo a cada chamada.
    """

    def __init__(self, model_name: str | None = None):
        self.model_name = model_name or settings.MODEL_NAME
        self._processor: Any = None
        self._model: Any = None

    def _load_model(self) -> tuple[Any, Any]:
        if self._processor is None or self._model is None:
            self._processor = BlipProcessor.from_pretrained(self.model_name)
            model: Any = BlipForConditionalGeneration.from_pretrained(self.model_name)
            self._model = model.to("cpu")
        assert self._processor is not None
        assert self._model is not None
        return self._processor, self._model

    def describe_image(self, image_path: str) -> str:
        processor, model = self._load_model()
        raw_image = Image.open(image_path).convert("RGB")

        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=50)
        return processor.decode(out[0], skip_special_tokens=True)
