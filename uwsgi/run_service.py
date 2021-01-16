import os

if __name__ == "__main__":
    print("working dir:%s" % os.getcwd())
    import service
    service.app.run(port=10000, debug=True, use_reloader=False)
