from absl import app

def main(argv):
    del argv
    print("The main entry point of the global command line interface.")
    
if __name__ == "__main__":
    app.run(main)