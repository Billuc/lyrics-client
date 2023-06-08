from vcr import VCR

my_vcr = VCR(path_transformer=VCR.ensure_suffix(".yml"), cassette_library_dir="tests/cassettes")