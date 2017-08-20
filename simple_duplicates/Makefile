clean:
	rm -f test_dir/obj
	rm -f test_dir/data.csv

test:
	find test_dir/ -type f -printf "%h %f %s\n" | python main.py -t f -d test_dir/obj -c test_dir/data.csv
