/** @odoo-module **/
import public_widget from "web.public.widget";
import { qweb } from "web.core";

export default public_widget.registry.get_data_user =
  public_widget.Widget.extend({
    selector: ".user",
    /**
     *@override
     **/
    start: function () {
      // let _contact = this.el.querySelector(".contact");
      this.getdata();
    },
    getdata: function () {
      this._rpc({
        route: "/get/data/user",
        params: {},
      }).then((r) => {
        this.get_dataUser(r);
      });
    },
    get_dataUser: function (data) {
      let template = "odoo_snippet.data_user";
      let out = qweb.render(template, { data: data });

      let _data_user = this.el.querySelector(".data_user");
      if (_data_user) {
        _data_user.innerHTML = out;
      }
    },
  });
