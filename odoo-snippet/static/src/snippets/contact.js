/** @odoo-module **/
import public_widget from "web.public.widget";
import { qweb } from "web.core";

export default public_widget.registry.get_data_contact =
    public_widget.Widget.extend({
        selector: ".contact",
        /**
        *@override
        **/
        start: function () {
            // let _contact = this.el.querySelector(".contact");
            this.getdata();
        },
        getdata: function () {
            this._rpc({
                route: "/get/data",
                params: {},
            }).then((r) => {
                this.get_contact(r);
            });
        },
        get_contact: function (r) {
            let template = "odoo_snippet.data_contact";
            
            let out = qweb.render(template, { results: r});
            let _contact = this.el.querySelector(".contact_data");
             if (_contact) {
                 _contact.innerHTML = out;
             }
        }
    });