# Operator pages

**The pages an instance's operator answers for (imprint, privacy policy, terms, the words of a pricing page, a notice on the start page) are Markdown files of the operator's, each named by a setting; the app ships none of the texts. A hosted instance keeps its public texts in its product's `stacks` repository, its contracts in the product's private `legal` repository, and its operator guide in the deployment's docs on the internal docs site.** Decided 2026-11-02.

## Why

The texts belong to whoever runs the instance, not to the app: a German operator needs an imprint and a privacy policy that name them, a self-hoster's family instance needs none, and the hosted instance's terms change without a release. Written into the app, they would be wrong for every instance but one and need a deploy to fix. notefeed moved its last built-in text, the license page, out of the app for this reason (notefeed ADR 0035).

How selling is set up on the hosted instance (which products, webhooks, settings and secrets) is a third kind of text: needed by the operator, of no use and partly sensitive for anyone else. It has no place in the app's public docs, and a wiki page about it goes stale with the next deploy ([docs live with the code](docs-live-with-the-code.md)).

## How

- **One setting per file:** `<APP>_IMPRINT_FILE`, `<APP>_PRIVACY_FILE`, `<APP>_TERMS_FILE`, `<APP>_NOTICE_FILE`, and the pricing page's words (`<APP>_LICENSE_FILE` in notefeed) while a payment provider is set. Each names a Markdown file, mounted read-only into the container.
- **No file, no page.** Without the setting, or with a file that can't be read, the page doesn't exist and the footer has no link to it. A file a page cannot do without (the pricing page's words while payments are on) stops the start and names the setting or the field, never the text.
- **A size limit** (a few hundred KB) on each file: a page of text, not a place to keep files.
- **Every language** the UI has ([language](../code/language.md)): one file per language, or one file with a section per language, as the app documents.
- **Where a hosted instance keeps them:**

  | What | Where | Who reads it |
  |---|---|---|
  | Imprint, privacy policy, terms, pricing words | the product's `stacks` repository, next to the compose file (`<app>/legal/*.md`), mounted into the container | everyone, through the app |
  | Contracts, data-processing agreements, drafts | the product's private `legal` repository ([where a repository lives](where-a-repo-lives.md)) | the operator |
  | The operator guide: products, webhooks, setting and secret names (never values), how to go live | `docs/` of the deployment or `stacks` repository | the operator, on the internal docs site |

- **The internal docs site** is one MkDocs site built from the `docs/` of the business's deployment and stacks repositories at each deploy, served behind the same sign-in as the other internal tools. A repository whose docs should be there is added to the site's list of repositories; nothing is copied by hand.
- **The app's public docs** say how to set the files on a self-hosted instance, and nothing about how the hosted instance sells.

## Rules out

- Legal texts, prices or the operator's name written into the app's code, copy modules or public docs.
- A footer link to a page that doesn't exist on this instance.
- Contracts or the operator guide in a public repository; setup steps for the hosted instance on a wiki page.
- A secret's value in any of these files.

## Reference

notefeed: `backend/legal.ts`, ADR 0035; its texts in `notefeed/stacks` (`notefeed/legal/`), its contracts in `notefeed/legal`, and its operator guide for licenses in the business's deployment repository, on the internal docs site. Gamepanion adds its pages for its subscription (gamepanion/gamepanion#48).
