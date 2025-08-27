from convert import ans_to_fan, fan_to_ans


def tests():
	# TEST 1 -- Convert an ANSI to FAN and then back to ANSI.
	print()
	print('==== TEST 1 - ANSI to FAN and back ====')
	ans_to_fan(
		ans_path='tests/TEST1.ANS',
		fan_path='tests/TEST1CNV.FAN',
		png_path='tests/TEST1CNV.PNG',
		png_scale=4,
	)
	fan_to_ans(
		fan_path='tests/TEST1CNV.FAN',
		ans_path='tests/TEST1_ROUNDTRIP.ANS',
		png_path='tests/TEST1_ROUNDTRIP.PNG',
		png_scale=4,
	)

	# TEST 2 -- Convert a FAN to ANSI and then back to FAN.
	print()
	print('==== TEST 2 - FAN to ANSI and back ====')
	fan_to_ans(
		fan_path='tests/TEST2.FAN',
		ans_path='tests/TEST2CNV.ANS',
		png_path='tests/TEST2CNV.PNG',
		png_scale=4,
	)
	ans_to_fan(
		ans_path='tests/TEST2CNV.ANS',
		fan_path='tests/TEST2_ROUNDTRIP.FAN',
		png_path='tests/TEST2_ROUNDTRIP.PNG',
		png_scale=4,
	)

	# TEST 3 -- Convert an oversized ANSI to FAN and back.
	print()
	print('==== TEST 3 - Oversized ANSI to FAN and back ====')
	ans_to_fan(
		ans_path='tests/TEST3.ANS',
		fan_path='tests/TEST3CNV.FAN',
		png_path='tests/TEST3CNV.PNG',
		png_scale=4,
	)
	fan_to_ans(
		fan_path='tests/TEST3CNV.FAN',
		ans_path='tests/TEST3_ROUNDTRIP.ANS',
		png_path='tests/TEST3_ROUNDTRIP.PNG',
		png_scale=4,
	)

	# TEST 4 -- Convert a plain text file to FAN and back.
	print()
	print('==== TEST 4 - Plain text file to FAN ====')
	ans_to_fan(
		ans_path='tests/TEST4.TXT',
		fan_path='tests/TEST4CNV.FAN',
		png_path='tests/TEST4CNV.PNG',
		png_scale=4,
	)
	print()


if __name__ == '__main__':
	tests()
