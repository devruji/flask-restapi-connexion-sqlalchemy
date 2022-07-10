from routes.route import app

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(port=5000, debug=True)