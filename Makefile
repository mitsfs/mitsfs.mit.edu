

serve:
	cactus serve

dev:
	cactus build

production:
	cactus build -c production.json

install:
	rsync -avzl --del '.build/' athena.dialup.mit.edu:/mit/mitsfs/web_scripts/mitsfs.mit.edu/

clean:
	$(RM) -r .build/ .sass-cache/ static/css/ pages/reviews/ static/scheduler/*.js