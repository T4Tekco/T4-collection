/** @odoo-module **/
import public_widget from "web.public.widget";
import { qweb } from "web.core";

export default public_widget.registry.get_slide_carousel =
  public_widget.Widget.extend({
    selector: ".carousel_slide_data",
    /**
     *@override
     **/
    start: function () {
      // let _contact = this.el.querySelector(".contact");
      this.getdata();
    },
    getdata: function () {
      this._rpc({
        route: "/get/slide",
        params: {},
      }).then((r) => {
        this.get_data_slide(r);
      });
    },
    get_data_slide: function (r) {
        let template = "odoo_snippet.carousel_slide";
        let [first, ...last] = r
        let out = qweb.render(template, { results: last,first:first });
        let _slide = this.el.querySelector(".slide_carousel");
        if (_slide) {
        _slide.innerHTML = out;
      }
    },
  });
