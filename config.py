+ #/Hello-Books/config.py

	class Config(object):
+  	  """Parent config class."""
+   	 DEBUG = False
		CSRF_ENABLED =True
+    	SECRET =("SECRET")
+

+
+
+	class DevelopmentConfig(Config):
+    """Configurations for development"""
+    DEBUG = True
+
+
+class TestingConfig(Config):
	"""configurations for development."""
	 DEBUG = True


+
+app_config = {
+    'development': DevelopmentConfig,
+    'testing': TestingConfig
	
+}