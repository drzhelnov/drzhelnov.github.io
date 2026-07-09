# README

## What this is

`assets/chats/` contains
transcripts from chatbot apps
like ChatGPT\.com or Claude\.ai.

The directory is arranged the following way:

```
.
├── yyyy-mm-dd-something-a
│   ├── some-chat.md
│   ├── some-other-chat.md
│   ├── …
│   └── raw
│       ├── some-chat.json
│       └── some-other-chat.json
│       └── …
├── yyyy-mm-dd-something-b
│   ├── some-chat.md
│   ├── some-other-chat.md
│   ├── …
│   └── raw
│       ├── some-chat.json
│       └── some-other-chat.json
│       └── …
├── …
└── README.md
```

Human-readable transcripts are
located in the `*.md` files
inside the subdirectories.
Apart from the complete chat log,
these files also contain chat metadata
(e.g., dates and model name).
These Markdown files are produced from
the `raw/*.json` files 
inside the subdirectories
using my custom code:
<https://github.com/paveljee/chat-viewer>

> [!NOTE]
> Because the
> conversion was automated
> from API responses,
> the chat URLs
> in the Markdown files are
> original private URLs
> rather than public-shareable and
> may not work as a result.
>
> However,
> when these are rendered as
> Jekyll pages
> (from symlinks in `_includes` and
> using `_layouts/chat.html`)
> the URLs are dynamically replaced
> with the public ones,
> whenever available,
> sourced from the
> individual page frontmatter.

## Acknowledgments

My `chat-viewer` uses Tampermonkey exporter outputs and scripts as reference material. Thanks to their authors:

Claude API Exporter 5.4.1 by MRL
https://update.greasyfork.org/scripts/542117/Claude%20API%20Exporter.user.js

ChatGPT Exporter 2.32.0 by pionxzh
https://update.greasyfork.org/scripts/456055/ChatGPT%20Exporter.user.js
