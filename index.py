from routing import app
import time

def run_every_five_secs():
    print("It works?")

if __name__ == '__main__':
    app.run(debug=True)
    run_every_five_secs()
    time.sleep(5)