import reflex as rx


@rx.memo
def index_colors() -> rx.Component:
    return rx.el.style(
        """
        .light,
.light-theme {
  /* Slate */
  --c-slate-1: #FCFCFD;
  --c-slate-2: #F9F9FB;
  --c-slate-3: #E8E8EC;
  --c-slate-4: #E8E8EC;
  --c-slate-5: #E0E1E6;
  --c-slate-6: #D9D9E0;
  --c-slate-7: #CDCED6;
  --c-slate-8: #B9BBC6;
  --c-slate-9: #8B8D98;
  --c-slate-10: #80838D;
  --c-slate-11: #60646C;
  --c-slate-12: #1C2024;
}

.dark,
.dark-theme {
  /* Slate */
  --c-slate-1: #151618;
  --c-slate-2: #1A1B1D;
  --c-slate-3: #222326;
  --c-slate-4: #27282B;
  --c-slate-5: #303236;
  --c-slate-6: #4B4D53;
  --c-slate-7: #5E5F69;
  --c-slate-9: #9A9CAC;
  --c-slate-8: #6E7287;
  --c-slate-10: #D9D9E0;
  --c-slate-11: #E0E1E6;
  --c-slate-12: #FCFCFD;
}
        """,
    )
