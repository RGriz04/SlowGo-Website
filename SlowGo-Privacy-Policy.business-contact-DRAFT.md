**Status: DRAFT (2026-10-17). Not applied to `SlowGo-Privacy-Policy.md` or `privacy.html`, not published.**
For Ron. The live policy's meaning is unchanged. Written against the live text (Last updated: October 12,
2026). The source of truth for the policy is the app repo's `SlowGo-Privacy-Policy.md`; when ruled, the
edits go there first, then this repo's copy, `privacy.html` and the sitemap `lastmod`, in one pass
(docs/site-README.md, "Legal pages"). Privacy-specialist review is deferred until fleet customers pay
(Ron, 2026-10-05); this draft is queued for that review.

# Privacy Policy amendment: business contact forms (/business and /business/setup)

## Why it's needed

The live policy says the Site has **two** forms (waitlist, town request) and that "nothing else is
asked for". The /business page adds five interest forms, and /business/setup adds a setup form with a
logo, phone numbers, a return-spot location and a shipping address. Publishing them without this
amendment would make the policy's "two forms" sentence untrue. **Deploy this amendment with the forms
or before them, never after.**

## The privacy line under each business form (already on the drafts, short version)

> We use what you send only to write back to you about SlowGo for your business. It is stored by
> Netlify, our website host, and you can ask us to delete it any time at hello@slowgoapp.com.
> Privacy Policy.

On the setup form:

> This goes only to Ron. He uses it to set up your shop in SlowGo and print your cards. It is stored by
> Netlify, our website host. Privacy Policy.

## Proposed policy text (four edits)

**1. Section 1, "Information you give us through the Site's forms"**, replace the paragraph with:

> **Information you give us through the Site's forms.** The Site has a waitlist form, which asks for
> your email address, and a town-request form, which asks for your email address and the name of a town
> or community. Our page for businesses (slowgoapp.com/business) has short contact forms for rental
> shops, dealers, communities, towns and tourism boards, and partners, which ask for your name, your
> organization's name, its town and state, and your email address, and may ask a little about the
> organization (such as how many carts it rents). A business that agrees to work with us may fill in a
> private setup form with its logo, phone numbers, the location riders return carts to, opening hours,
> places it recommends, and a shipping address for its cards. All of these forms are optional, and none
> is part of the App. Section 3 describes what happens to what you submit.

**2. Section 3, the Netlify row**: change "receives what you submit through its waitlist and
town-request forms" to "receives what you submit through the Site's forms", and in the right-hand
column add after "that you type into a Site form": "(for a business form, the contact and business
details described in Section 1, and any logo file you upload)".

**3. Section 3, a new sub-section after "The Site's waitlist and town-request forms":**

> ### Business contact and setup forms
>
> We use what a business sends through these forms to reply to it, to discuss working together, and,
> for a business that signs up, to set up its card, its link and its listing in the App, and to ship
> its cards. **We do not sell this information, we do not share it for advertising, and we do not add
> you to a mailing list.** A business's name, logo, phone number, return spot and recommended places
> are shown to riders in the App and on its cards only after the business has agreed to that. The
> person's own name, email address and the shipping address are never shown to riders.
>
> Submissions are stored by **Netlify**, which hosts the Site, as our service provider. We keep a
> business contact submission for up to 24 months after our last exchange with that business, or until
> you ask us to delete it, whichever comes first; for a business that signs up, we keep its setup
> details for as long as it works with us and for 24 months after, plus any records the law requires.
> To have a submission deleted, email hello@slowgoapp.com.

**4. Section 6 (Data Retention)**, after "…whichever comes first;" for waitlist and town requests, add:
"business contact and setup submissions are kept as described in Section 3;". In the **California
notice** (Section 9), change "the email address and town you may submit through a Site form" to "the
contact details you may submit through a Site form".

## Open questions for Ron (LEGAL)

1. **Retention periods** above (24 months) are proposals to match the policy's 24 months for emails;
   Ron picks.
2. **Material or not?** It adds new collection for a new audience (businesses), not new use of existing
   rider data. Proposed: not material for riders; it applies only to people who use the new forms.
   Ron rules.
3. **Netlify's PII note:** Netlify's form docs say forms that collect personally identifiable
   information need extra configuration and suggest a paid add-on. Proposed: not needed at this volume
   (business contact details, not sensitive data), but this is a question for the deferred
   privacy-specialist review.
4. **If an auto-reply service is ever added** (Zapier/n8n or an email API; docs/business-forms.md), it
   becomes a new processor and needs its own row in Section 3 before it goes on.
5. The fleet-mode amendment (app repo `docs/legal-drafts/privacy-fleet-v1-draft.md` on f16-fleet) is a
   separate draft; the two should be merged into one dated update if they ship together.
