from website import create_app

app = create_app()

if __name__ == '__main__': # run the app
    app.run(debug=True) # rerun webserver on code changes