import sentry_sdk

import time

sentry_sdk.init(
    dsn="https://677c7b3225e6caa5cb6a20ea3ccb4911@o4505699197452288.ingest.sentry.io/4506830834761728",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

sentry_sdk.capture_message("teste de mensagem")
time.sleep(3)
time.sleep(3)