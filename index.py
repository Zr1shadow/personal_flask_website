from routing import app
import time



if __name__ == '__main__':
    app.run(debug=True)
    run_every_five_secs()
    time.sleep(5)