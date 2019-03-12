class ProcesadorMensajes:

    def __init__(self):
        self.mensajes = {
            "MedicionCompleta": "finalizar_medicion",
            "CerrarPantallaEspera": "cerrar",
            "LundebyException": "mostrar_error_lundeby",
            "ActivarBotonInstrucciones": "activar_boton_instrucciones",
            "ActivarBotonVistaDetallada": "activar_boton_vista_detallada",
            "CalculoCompleto": "finalizar_calculo"
        }

    def get_mensaje(self, clave_mensaje):
        return self.mensajes.get(clave_mensaje)
