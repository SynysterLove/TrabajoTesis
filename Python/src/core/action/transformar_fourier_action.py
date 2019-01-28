from src.core.provider.service_provider import ServiceProvider


class TransformarFourierAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def execute(self, senal_en_tiempo, fs):
        return self.operaciones_service.transformar_fourier(senal_en_tiempo, fs)

