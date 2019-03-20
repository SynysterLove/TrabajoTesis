from rx.subjects import Subject


class SubjectProvider:

    pantalla_principal_subject = None
    vista_detallada_subject = None
    pantalla_espera_subject = None

    @classmethod
    def provide_pantalla_principal_subject(cls):

        if cls.pantalla_principal_subject is None:
            cls.pantalla_principal_subject = Subject()

        return cls.pantalla_principal_subject

    @classmethod
    def provide_vista_detallada_subject(cls):

        if cls.vista_detallada_subject is None:
            cls.vista_detallada_subject = Subject()

        return cls.vista_detallada_subject

    @classmethod
    def provide_pantalla_espera_subject(cls):

        if cls.pantalla_espera_subject is None:
            cls.pantalla_espera_subject = Subject()

        return cls.pantalla_espera_subject

