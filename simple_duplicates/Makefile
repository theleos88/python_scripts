clean:
	rm -f results/*

test:
	find test_dir/ -type f -printf "%h %f %s " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \; |  python main.py -t f -d results/obj -c results/data.csv

showtest:
	find test_dir/ -type f -printf "%h %f %s " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \; |  python main.py -t f -d results/obj -c results/data.csv -s results/obj
