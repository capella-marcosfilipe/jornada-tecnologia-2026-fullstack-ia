from backend.graph.state import AgentState
from backend.utils.image_processor import ImageProcessor

class VisionNode:
    def __init__(self):
        self.processor = ImageProcessor()

    def execute(self, state: AgentState) -> dict:
        print("--- EXECUTANDO VISÃO (BLIP) ---")
        if state is None:
            return {"raw_description": None}
        image_path = state["image_path"]
        
        # Extrai a legenda bruta da imagem
        description = self.processor.describe_image(image_path)
        
        return {"raw_description": description}