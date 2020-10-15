import struct, os


def file_hash(name) -> str:
    """
    Calculate OpenSubtitle video hash.
    https://trac.opensubtitles.org/projects/opensubtitles/wiki/HashSourceCodes#Python

    param name: file name
    returns: file hash or IOError
    """
    try:

        longlongformat = '<q'  # little-endian long long
        bytesize = struct.calcsize(longlongformat)
        f = open(name, "rb")

        filesize = os.path.getsize(name)
        hash = filesize

        if filesize < 65536 * 2:
            return "SizeError"

        for x in range(int(65536 / bytesize)):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF  #to remain as 64bit number

        f.seek(max(0, filesize - 65536), 0)
        for x in range(int(65536 / bytesize)):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF

        f.close()
        returnedhash = "%016x" % hash
        return returnedhash

    except (IOError):
        return "IOError"

