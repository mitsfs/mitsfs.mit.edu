# MITSFS Static Website Generator


## Building using Docker

```
docker build . -t mitsfs
docker run --rm -iv${PWD}:/host mitsfs sh -s <<EOF
  chown -vR $(id -u):$(id -g) .build
  cp -rva .build/ /host/
EOF
```


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
