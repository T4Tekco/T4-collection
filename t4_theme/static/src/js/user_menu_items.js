/** @odoo-module **/

import { registry } from "@web/core/registry";
import { UserMenu } from "@web/webclient/user_menu/user_menu";
import { patch } from "@web/core/utils/patch";

const user_menuitems = registry.category("user_menuitems");

patch(UserMenu.prototype, "t4tek_theme.UserMenu", {
  setup() {
    this._super.apply(this, arguments);
    user_menuitems.remove("documentation");
    user_menuitems.remove("support");
    user_menuitems.remove("shortcuts");
    user_menuitems.remove("separator");
    user_menuitems.remove("profile");
    user_menuitems.remove("odoo_account");
  },
});
