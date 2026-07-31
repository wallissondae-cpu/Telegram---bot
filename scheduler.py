from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone="UTC")


def iniciar_scheduler():
    print("Scheduler iniciado.", flush=True)
    scheduler.start()
