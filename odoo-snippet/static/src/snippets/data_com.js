/** @odoo-module **/
import public_widget from "web.public.widget";
import { qweb } from "web.core";

export default public_widget.registry.get_data_company =
  public_widget.Widget.extend({
    selector: ".com",
    /**
     *@override
     **/
    start: function () {
      // let _contact = this.el.querySelector(".contact");
      this.getdata();
    },
    getdata: function () {
      this._rpc({
        route: "/get/data_company",
        params: {},
      }).then((r) => {
        this.get_dataCompany(r);
      });
    },
    get_dataCompany: function (data) {
      let template = "odoo_snippet.data_company";
      let out = qweb.render(template, { data: data[0] });

      let _data_com = this.el.querySelector(".data_company");
      if (_data_com) {
        _data_com.innerHTML = out;
      }
    },
  });
