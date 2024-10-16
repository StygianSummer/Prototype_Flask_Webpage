from Website import create_app

app = create_app()
if __name__ == '__main__':
    #only if we run main.py, we run the web server
    app.run(debug=True)
    #reruns the website everytime we make a change, remove in production
