

serve:
	cactus serve

dev:
	cactus build

production:
	cactus build -c production.json

install_production:
	rsync -avzl --del '.build/' /mit/mitsfs/ookcomm/production

install_dev:
	rsync -avzl --del '.build/' /mit/mitsfs/ookcomm/dev

install_production_remote:
	rsync -avzl --del '.build/' athena.dialup.mit.edu:/mit/mitsfs/ookcomm/production

install_dev_remote:
	rsync -avzl --del '.build/' athena.dialup.mit.edu:/mit/mitsfs/ookcomm/dev

clean:
	$(RM) -r .build/ .sass-cache/ static/css/ pages/reviews/ static/scheduler/*.js
