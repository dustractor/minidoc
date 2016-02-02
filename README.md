# minidoc
---

#### Example Session:

    >>> import minidoc
    >>> a = minidoc.elem("foo")
    >>> print(a)
    <foo/>

    >>> b = minidoc.elem("bar").attrs(baz=123)
    >>> print(b)
    <bar baz="123"/>

    >>> a += b
    >>> print(a)
    <foo>
            <bar baz="123"/>
    </foo>

    >>> b.attrs(baz="zap")
    <DOM Element: bar at 0x103993a60>
    >>> print(a)
    <foo>
            <bar baz="zap"/>
    </foo>

    >>> a.txt("foo text bar")
    <DOM Element: foo at 0x1039939c8>
    >>> print(a)
    <foo>
            <bar baz="zap"/>
            foo text bar
    </foo>

    >>> c = minidoc.elem("bop")
    >>> c.cdata("123abc")
    <DOM Element: bop at 0x103993df0>
    >>> a += c
    >>> print(a)
    <foo>
            <bar baz="zap"/>
            foo text bar
            <bop>
    <![CDATA[123abc]]>	</bop>
    </foo>

    >>> z = minidoc.elem("div").attrs(**{"class":"foobop","id":"zipzap"})
    >>> b += z
    >>> print(a)
    <foo>
            <bar baz="zap">
                    <div class="foobop" id="zipzap"/>
            </bar>
            foo text bar
            <bop>
    <![CDATA[123abc]]>	</bop>
    </foo>

    >>> z += minidoc.elem("p").txt("Hello").attrt(("class","world"))
    >>> print(a)
    <foo>
            <bar baz="zap">
                    <div class="foobop" id="zipzap">
                            <p class="special_p">Hello World</p>
                    </div>
            </bar>
            foo text bar
            <bop>
    <![CDATA[123abc]]>	</bop>
    </foo>

