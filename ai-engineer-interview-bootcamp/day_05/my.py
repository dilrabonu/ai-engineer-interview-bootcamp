class AnalyzerText:
    """ Analyze the text"""
    def __init__(self, text):
        self.text = text
        self.words = []
        self.words_count = {}
        self._process_text()

    def _process_text(self):
        """ Process the text and split"""
        clean_text = self.text.lower()

        punctuation = "/?!@#$%^&*(/*.,)"
        for char in punctuation:
            clean_text = clean_text.replace(char, "")
        self.words = clean_text.split()

        for word in self.words:
            if word in self.words_count:
                self.words_count[word] + 1
            else:
                self.words_count[word] = 1

    def get_longest_word(self):
        if not self.words:
            return None
        longest = ""
        for word in self.words:
            if len(word) > len(longest):
                longest = word
        return longest

    def export_report(self, filename="report.txt"):
        with open("report.txt", "w") as file:
            file.write("="*50 + "\n")
            file.write("TEXT ANALYZE REPORT\n")

text = " I have taken an offer from Google for the postion AI/ML Engineer. I am so happy"
analyzer = AnalyzerText(text)
analyzer.export_report("my_report.txt")
print(f" The longest word is: {analyzer.get_longest_word()}")
print(f"Word count: {analyzer.words_count}")
print(f"Words: {analyzer.words}")
