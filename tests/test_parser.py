import unittest
import random
from io import StringIO
import tempfile


from lobster.parser import validate_line, parse_tracks_file
from lobster.exceptions import InputFileException

class TestParserMethods(unittest.TestCase):

    def test_validate_line_valid_line(self):
        test_line = "test track |11:11"
        assert validate_line(test_line.split("|"), 1) is True

    def test_validate_line_invalid_line_empty_name(self):
        test_line = "|11:11"

        self.assertRaises(InputFileException, validate_line, test_line, 1)
    
    def test_validate_line_invalid_line_empty_start_time(self):
        test_line = "song title|"

        self.assertRaises(InputFileException, validate_line, test_line, 1)
    
    def test_validate_line_invalid_line_invalid_start_time(self):
        test_line = "song title|asdasd"

        self.assertRaises(InputFileException, validate_line, test_line, 1)

    def test_parse_tracks_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b"Test track 1|00:00\n")
            f.write(b"Test track 2|05:30\n")
            f.close()
            tracks_file_stream_segments = parse_tracks_file(f.name)
        assert(len(tracks_file_stream_segments) == 2)
        assert(tracks_file_stream_segments[0].name == "Test track 1")
        assert(tracks_file_stream_segments[0].end_time == None)
        assert(tracks_file_stream_segments[0].initial_time == "00:00\n")
        assert(tracks_file_stream_segments[1].name == "Test track 2")
        assert(tracks_file_stream_segments[1].end_time == None)
        assert(tracks_file_stream_segments[1].initial_time == "05:30\n")
        
    def test_parse_invalid_tracks_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b"|00:00\n")
            f.write(b"Test track 2|05:30\n")
            f.close()
            self.assertRaises(InputFileException, parse_tracks_file, f.name)


if __name__ == '__main__':
    unittest.main()