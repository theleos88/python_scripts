DATA=test_dir/
OBJ=/tmp/obj
CSV=/tmp/data.csv

.DEFAULT_GOAL := all

clean:
	rm -f results/*

test:
	find test_dir/ -type f -printf "%h þ %f þ %s þ " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \; |  python main.py -t f -d results/obj -c results/data.csv

showtest:
	find test_dir/ -type f -printf "%h þ %f þ %s þ " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \; |  python main.py -t f -d results/obj -c results/data.csv -s results/obj

all:
	find $(DATA) -type f -printf "%h þ %f þ %s þ " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \; | python main.py -t f -d $(OBJ) -c $(CSV)

show:
	find $(DATA) -type f -printf "%h þ %f þ %s þ " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \; | python main.py -t f -s $(OBJ)

find:
	find $(DATA) -type f -printf "%h þ %f þ %s þ " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \;

human:
	find $(DATA) -type f -printf "%h ||| %f ||| %s ||| " -exec bash -c 'xxd -p -l 10 "$$1"' - {} \; >> $(OBJ)