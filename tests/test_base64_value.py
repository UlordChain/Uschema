import base64


def base64_to_hex(b64_data):
	src_data = base64.b64decode(b64_data)
	return src_data.encode('hex')


def main():
    data1 = "CAEQAiJeCAEQAyJYMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEDqRRc8HIYpQWzZKLUMTZamDgA5e7rJkyCsCTqMJwvLAF26rOtDFQdEghMUHuwEVLfqNdHyPB4KJIPPRqhZF+0w== "
    hex_data = base64_to_hex(data1)

    pass


if __name__ == '__main__':
    main()
    