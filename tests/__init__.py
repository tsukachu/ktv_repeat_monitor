from simple_settings import settings

settings.DATABASE["NAME"] = "test_" + settings.DATABASE["NAME"]
settings.configure(DATABASE=settings.DATABASE)
