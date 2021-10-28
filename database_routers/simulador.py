class SimuladorRouter:
    """
    A router to control all database operations on models in the
    home application.
    """
    route_app_labels = {'home'}
   
    def db_for_read(self, model, **hints):
        """
        Attempts to read home models go to simulador.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'simulador'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write home models go to simulador.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'simulador'
        return None