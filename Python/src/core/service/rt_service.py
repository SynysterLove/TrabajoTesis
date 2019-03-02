class RTService:

    def __init__(self):
        self.tiempos_reverberacion = {
            "EDT": self.calcular_edt,
            "T20": self.calcular_t20,
            "T30": self.calcular_t30,
        }
        from src.core.provider.service_provider import ServiceProvider
        self.recortar_service = ServiceProvider.provide_recortar_senales_service()
        self.estadistica_service = ServiceProvider.provide_estadistica_service()

    def calcular_rt(self, curva_decaimiento, rt):
        return self.tiempos_reverberacion.get(rt)(curva_decaimiento)

    def calcular_edt(self, curva_decaimiento):
        segmento = self.recortar_service.recortar_intervalo_en_amplitud_hasta_violar_condicion(curva_decaimiento, -10, 0)
        return self.calcular_tiempo_en_menos_60_db(segmento)

    def calcular_t20(self, curva_decaimiento):
        segmento = self.recortar_service.recortar_intervalo_en_amplitud_hasta_violar_condicion(curva_decaimiento, -25, -5)
        return self.calcular_tiempo_en_menos_60_db(segmento)

    def calcular_t30(self, curva_decaimiento):
        segmento = self.recortar_service.recortar_intervalo_en_amplitud_hasta_violar_condicion(curva_decaimiento, -35, -5)
        return self.calcular_tiempo_en_menos_60_db(segmento)

    def calcular_tiempo_en_menos_60_db(self, segmento):
        recta_regresion = self.estadistica_service.efectuar_regresion_lineal(
            segmento.get_dominio_temporal(), segmento.get_valores())
        return recta_regresion.get_preimagen(-60)


