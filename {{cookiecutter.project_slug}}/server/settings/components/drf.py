# -*- coding: utf-8 -*-

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "apps.users.rest.authentication.TokenAuthentication",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "NON_FIELD_ERRORS_KEY": "detail",
    "SEARCH_PARAM": "q",
}

REST_FRAMEWORK_TOKEN_EXPIRE = 60 * 24 * 30  # mins
