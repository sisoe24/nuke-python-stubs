import re

import PySide2


class UsdHighlighter(PySide2.QtGui.QSyntaxHighlighter):
    def __init__(self, doc, parent=None):
        super(UsdHighlighter, self).__init__(parent)

        self.setDocument(doc)

        self._rules = []

        self._keywords = PySide2.QtGui.QTextCharFormat()
        self._keywords.setForeground(PySide2.QtGui.QColor(112, 225, 128))
        self._keywords.setFontWeight(PySide2.QtGui.QFont.Bold)
        self._rules.append(
            {
                'pattern': '\\b(def|class|over|variantSet|inherits|rel|add|append|prepend|delete|varying|uniform|custom)\\b',
                'format': self._keywords
            }
        )

        self._types = PySide2.QtGui.QTextCharFormat()
        self._types.setForeground(PySide2.QtGui.QColor(156, 208, 255))
        self._rules.append(
            {
                'pattern': '\\b(asset|bool|uchar|int|uint|int64|uint64|half|float|double|string|token|\
matrix2d|matrix3d|matrix4d|quatd|quatf|quath|\
double2|float2|half2|int2|double3|float3|half3|int3|double4|float4|half4|int4|rel)\\b',
                'format': self._types
            }
        )
        self._rules.append(
            {
                'pattern': '\\b(point3d|point3f|point3h|\
normal3d|normal3f|normal3h|vector3d|vector3f|vector3h|\
color3d|color3f|color3h|color4d|color4f|color4h|\
frame4d|texCoord2h|texCoord2d|texCoord2f|texCoord3h|texCoord3d|texCoord3f)\\b',
                'format': self._types
            }
        )

        # String Literals
        self._strings = PySide2.QtGui.QTextCharFormat()
        self._strings.setForeground(PySide2.QtGui.QColor(226, 138, 138))
        self._rules.append(
            {
                'pattern': '"([^"\\\\]|\\\\.)*"',
                'format': self._strings
            }
        )

        # Paths
        self._paths = PySide2.QtGui.QTextCharFormat()
        self._paths.setForeground(PySide2.QtGui.QColor(255, 220, 120))
        self._rules.append(
            {
                'pattern': '\\<[^\\>]*\\>',
                'format': self._paths
            }
        )

        # Assets
        self._assets = PySide2.QtGui.QTextCharFormat()
        self._assets.setForeground(PySide2.QtGui.QColor(255, 120, 220))
        self._rules.append(
            {
                'pattern': '@[^@]*@',
                'format': self._assets
            }
        )

        # Comments
        self._comment = PySide2.QtGui.QTextCharFormat()
        self._comment.setForeground(PySide2.QtGui.QColor(188, 179, 84))
        self._rules.append(
            {
                'pattern': '#[^\n]*',
                'format': self._comment
            }
        )

    def highlightBlock(self, text):
        text = str(text)
        for rule in self._rules:
            expression = rule['pattern']

            if len(text) > 0:
                results = re.finditer(expression, text)

                # Loop through all results
                for result in results:
                    index = result.start()
                    length = result.end() - result.start()
                    self.setFormat(index, length, rule['format'])
