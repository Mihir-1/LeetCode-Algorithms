class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def justifyLine(line: str, left: bool) -> str:
            if left: 
                line += ' ' * (maxWidth - len(line))
            else:
                spaces = maxWidth - len(line)
                wordsArr = line.split(' ')
                joinBy = ' ' + ' ' * (spaces // (len(wordsArr) - 1))
                remaining = spaces % (len(wordsArr) - 1)
                line = wordsArr[0]
                for word in wordsArr[1:]:
                    line += joinBy
                    if remaining > 0:
                        line += ' '
                        remaining -= 1
                    line += word
            return line

        justified = []
        cur = ''
        for word in words:
            if len(cur) + len(word) > maxWidth:
                cur = cur[:-1]
                justified += [justifyLine(cur, len(cur.split(' ')) == 1)]
                cur = ''
            cur += word + ' '
        justified += [justifyLine(cur.strip(), True)]
        return justified

