# MITSFS Static Website Generator


## Contributing
Feel free to submit pull requests to contribute. If you are making small text
changes feel free to use the Github editor to make changes. Otherwise you will
probably need to learn git and test your changes.

## Testing Using Docker

This will build and run a test server using docker. Currently you will have to
rerun the commands on a change.

```
docker build . -t mitsfs
docker run -p 8000:8000 mitsfs
```

## Building using Docker

This builds and copies the website to your .build directory.

```
docker build . -t mitsfs
docker run --rm -iv${PWD}:/host mitsfs sh -s <<EOF
  cactus build -c production.json
  chown -vR $(id -u):$(id -g) .build
  cp -rva .build/ /host/
EOF
```

## Deploying

### Dev

Once the build is built on master ssh to athena.dialup.mit.edu and run

`athrun mitsfs mitsfs-web-install`

Go to `http://web-test.mitsfs.scripts.mit.edu` to test

### Production

`athrun mitsfs mitsfs-web-install --production`

Go to `http://mitsfs.mit.edu` to test.



## Dependencies:

    pip install cactus

Yes this is dumb we don't actually need it but it breaks without it.

Cactus basically requires a deployment engine and there is none for the local filesystem so we will pretent to use google for now.

    pip install google-api-python-client==1.2

Also you must install

- sass >= 3.3.0

For production builds (mac)

- closure-compilier
- yuicompressor

### ubuntu
    sudo apt-get install yui-compressor
    sudo apt-get install libclosure-compiler-java

## Testing

    make serve

## production - Athena

    make clean && make production 

### Install on Athena
    
    make install_production

### Install remote
    
    make install_production_remote
