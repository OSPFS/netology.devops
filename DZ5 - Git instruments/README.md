1. Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea.
```
git show aefea

aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Update CHANGELOG.md
```
2. Какому тегу соответствует коммит 85024d3?
```
git show 85024d3

tag: v0.12.23
```
3. Сколько родителей у коммита b8d720? Напишите их хеши.
```
git log --graph b8d720|more

*   commit b8d720f8340221f2146e4e4870bf2ee0bc48f2d5
|\  Merge: 56cd7859e 9ea88f22f
| | Author: Chris Griggs <cgriggs@hashicorp.com>
| | Date:   Tue Jan 21 17:45:48 2020 -0800
| |
| |     Merge pull request #23916 from hashicorp/cgriggs01-stable
| |
| |     [Cherrypick] community links
| |
| * commit 9ea88f22fc6269854151c571162c5bcf958bee2b
|/  Author: Chris Griggs <cgriggs@hashicorp.com>
|   Date:   Tue Jan 21 17:08:06 2020 -0800
|
|       add/update community provider listings
|
*   commit 56cd7859e05c36c06b56d013b55a252d0bb7e158
```

4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24
```
git log  --pretty=oneline v0.12.23..v0.12.24

33ff1c03bb960b332be3af2e333462dde88b279e v0.12.24
b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links
3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md
6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable
5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location
06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows
4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release
```
5. Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так func providerSource(...) (вместо троеточего перечислены аргументы).
```
git log -S 'func providerSource(' --oneline

commit 8c928e83589d90a031f811fae52a81be7153e82f
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Thu Apr 2 18:04:39 2020 -0700
```
6. Найдите все коммиты в которых была изменена функция globalPluginDirs.
```
git log -L:globalPluginDirs:plugins.go --oneline

78b122055
52dbf9483
41ab0aef7
66ebff90c
8364383c3
```
7. Кто автор функции synchronizedWriters? 
```
git log -S 'func synchronizedWriters'

commit 5ac311e2a91e381e2f52234668b49ba670aa0fe5
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Wed May 3 16:25:41 2017 -0700
```