from routes.route import app

# TODO: Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(port=5000, debug=True)