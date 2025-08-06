<script setup>
const navItems = [
  {
    header: null,
    items: [
      { title: 'Dashboard', to: '/dashboard', icon: 'mdi-view-dashboard' },
    ],
  },
  {
    header: 'User Management',
    items: [
      { title: 'Pharmacists', to: '/users/pharmacists', icon: 'mdi-account' },
      { title: 'Admins', to: '/users/admins', icon: 'mdi-account-key' },
    ],
  },
  {
    header: 'Inventory',
    items: [
      { title: 'Medications', to: '/inventory/medications', icon: 'mdi-pill' },
    ],
  },
  {
    header: 'Reports',
    items: [
      { title: 'Daily Sales', to: '/reports/daily-sales', icon: 'mdi-cash-register' },
      { title: 'Expired Items', to: '/reports/expired-items', icon: 'mdi-alert' },
    ],
  },
];
</script>

<template>
  <v-layout class="rounded rounded-md">
    <v-navigation-drawer>
      <v-list nav>
        <template v-for="(section, index) in navItems" :key="index">
          <v-list-subheader v-if="section.header">{{ section.header }}</v-list-subheader>

          <v-list-item
            v-for="(item, idx) in section.items"
            :key="idx"
            :title="item.title"
            :to="item.to"
            :prepend-icon="item.icon"
            link
          />
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar title="Pharmacy POS"></v-app-bar>

    <v-main class="main">
      <v-container class="px-4 bg-background" fluid>
        <router-view />
      </v-container>
    </v-main>
  </v-layout>
</template>
