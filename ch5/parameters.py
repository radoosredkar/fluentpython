param1 = list(range(3))
param2 = {"key%s" % value: value for value in list(range(2))}


def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs["class"] = cls
    if attrs:
        attr_str = ''.join(" %s=%s" % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))

    else:
        attr_str = ""

    if content:
        return "\n".join("<%s%s>%s</%s>" %
                         (name, attr_str, c, name) for c in content)
    else:
        return "<%s%s/>" % (name, attr_str)


print(tag('br'))
print(tag("p", "Hello"))
print(tag("h1", "Rado Osredkar", font="'tahoma'", size=12))
content = tag("ul", "Rado Osredkar", "Stara Cesta 45", "1360 Vrhnika", size=1)
print(tag("li", content))

my_tag = {'name': 'img', 'title': "'Sunset Boulevard'", 'src': "'sunset.jpg'", 'cls': "'framed'"}
print(tag(**my_tag))


# Keyword only arguments
def f(*, b):
    return b


print(f(b=1))

from ch5.clip import clip
print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)

from inspect import signature
sig = signature(clip)
print(sig)
print(str(sig))
print(sig.return_annotation)
for name, parameter in sig.parameters.items():
    print(name, parameter, parameter.default, parameter.kind)