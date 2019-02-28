import numpy

from src.core.domain.senal_audio import SenalAudio


class ObtenerCurvaDeDecaimientoAction:

    def __init__(self):
        from src.core.provider.action_provider import ActionProvider
        self.estimar_por_metodo_lundeby_action = ActionProvider.\
            provide_estimar_limite_superior_por_metodo_de_lundeby_action()
        self.integrar_senal = ActionProvider.provide_integrar_senal_action()
        self.transformar_a_db = ActionProvider.provide_transformar_a_escala_logaritmica_normalizada_action()

    def execute(self, respuesta_impulsional, fs):

        t = respuesta_impulsional.get_dominio_temporal()
        h = respuesta_impulsional.get_valores()
        estimacion = self.estimar_por_metodo_lundeby_action.execute(respuesta_impulsional, fs)
        t_limite = estimacion.get_limite()
        c_corr = estimacion.get_termino_correccion()
        h_cuadrado = numpy.power(h, 2)

        senal_h_cuadrado = SenalAudio(fs, t, h_cuadrado)
        s_cuadrado = self.calcular_integrar_de_schroeder(fs, senal_h_cuadrado, t_limite)
        s_cuadrado = self.aplicar_termino_de_correccion(c_corr, s_cuadrado)
        s_db = self.transformar_a_db.execute(s_cuadrado)
        return SenalAudio(fs, s_cuadrado.get_dominio_temporal(), s_db)


    def aplicar_termino_de_correccion(self, c_corr, s_cuadrado):
        valores = s_cuadrado.get_valores()
        return SenalAudio(s_cuadrado.get_fs(), s_cuadrado.get_dominio_temporal(), [valores[i] + c_corr for i in range(len(valores))])

    def calcular_integrar_de_schroeder(self, senal_h_cuadrado, fs, t_limite):
        t = senal_h_cuadrado.get_dominio_temporal()
        h_cuadrado = senal_h_cuadrado.get_valores()
        nuevo_dominio = numpy.linspace(0, t_limite, t_limite * fs)
        s_cuadrado = nuevo_dominio.copy()
        dx = 1 / fs
        s_cuadrado[0] = self.integrar_senal.execute(senal_h_cuadrado, t[0], t_limite)
        for i in range(len(s_cuadrado) - 1):
            s_cuadrado[i + 1] = s_cuadrado[i] - h_cuadrado[i] * dx

        return SenalAudio(fs, nuevo_dominio, s_cuadrado)
