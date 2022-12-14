<template lang="pug">
div  
  v-container
    h1.text-center.my-6 Discover Dishes
    v-row 
      v-col
        v-skeleton-loader(v-show="!loaded" :loading="!loaded" transition="fade-transition" type="card")
        template(v-if="loaded")
          v-data-iterator(:items='items' :items-per-page.sync='itemsPerPage' :page.sync='page' 
            hide-default-footer 
            :sort-desc="sortDesc")
            template(v-slot:header)
              v-toolbar.mb-2(color='primary' dark height='130px')
                v-col.py-0.mt-0(cols='12')
                  v-card(color="primary" flat)
                    v-col.d-flex.justify-space-between.py-0
                      v-text-field(v-model='search' clearable flat solo-inverted hide-details 
                        prepend-inner-icon='mdi-magnify' label='Search')
                      v-checkbox.mx-3.pt-3(
                        v-model="filters.affordable"
                        label="Affordable")
                      v-checkbox.mx-3.pt-3(
                        v-model="filters.main_dish"
                        label="Main Dish")
                  v-card(color="primary" flat)
                    v-col.align-center.justify-center.d-flex.justify-space-between.py-0
                      template(v-if='$vuetify.breakpoint.mdAndUp')
                        v-select(flat solo-inverted hide-details :items='Object.keys(filters.food_preferences)' width='100'
                          prepend-inner-icon='mdi-filter-variant' label='Filter Categories' multiple
                          v-model='selectedCategories')
            template(v-slot:default='props')
              v-row
                v-col(v-for='(item, index) in props.items' :key="index" cols='12' sm='6' md='6' lg='4')
                  v-card(height="100%")
                    v-img(v-show="item.dish.url != null" :alt="item.dish.name" height='250'
                    :src="item.dish.url")
                    v-card.center-items.light-green.lighten-2.rounded-b-0(v-show="item.dish.url == null" height='250')
                      h1 {{ item.dish.name[0] }}

                    v-card-title.subheading(style="word-break: normal")
                      | {{ item.dish.name }}
                    v-divider
                    v-col.align-center.justify-center.d-flex.justify-space-between.py-0
                      h4.ma-0.text-right.subheading(:class="{'red--text': $store.state.card_balance <= (parseFloat(item.priceStudent)+1) }")
                        //- (:class="{ 'primary--text': sortBy === key }")
                        | ???{{ item.priceStudent.replace('.',',') }}/{{ item.priceEmployee.replace('.',',') }}
                      v-img(v-for="(category, index) in item.dish.categories.length" :alt="item.dish.categories[index].category.name" 
                        height="50" max-width="50" contain :key="category"
                        :src="require('@/assets/dish_icons/food_preferences/'+item.dish.categories[index].category.name+'.png')")
                      v-btn(rounded :href="getGoogleMapsUrl(item.mensa.name)" target="_blank" rel="noopener noreferrer")
                        v-icon mdi-navigation-variant-outline
                        | {{ (item.mensa.name).replace('Bistro Katholische Hochschule', 'Bistro Katho.').replace('Bistro Oeconomicum','Oeconomicum') }}
                    v-col.align-center.justify-center.d-flex.justify-space-between
                      div
                        span
                          //- (:class="{ 'primary--text': sortBy === key }")
                          v-icon mdi-food-apple
                          | {{ item.dish.main ? 'Main Dish' : 'Side Dish' }}
                      div 
                        v-icon mdi-shield-plus-outline
                        span
                          //- (:class="{ 'primary--text': sortBy === key }")
                          span(v-if="item.dish.additives.length == 0")  None
                          span(v-for="additive in item.dish.additives" :key="additive.additive.name")  {{ additive.additive.name }}
                    v-col.align-center.justify-center.d-flex.justify-space-between
                      div 
                        v-icon mdi-calendar
                        span {{ new Date(item.date).toLocaleDateString('de-DE') }}
                      v-rating(hover length="5" background-color="gray" readonly size="24" half-increments 
                        v-model="parseFloat(item.ext_ratings.rating_avg) + 0.0")

            template(v-slot:footer)
              v-row.mt-2(align='center' justify='center')
                span.grey--text Items Per Page
                v-menu(offset-y)
                  template(v-slot:activator='{ on, attrs }')
                    v-btn.ml-2(dark text color='primary' v-bind='attrs' v-on='on')
                      | {{ itemsPerPage }}
                      v-icon mdi-chevron-down
                  v-list
                    v-list-item(v-for='(number, index) in itemsPerPageArray' :key='(number, index)' 
                      @click='updateItemsPerPage(number)')
                      v-list-item-title {{ number }}
                v-spacer
                span.mr-4.grey--text
                  | Page {{ page }} of {{ numberOfPages }}
                v-btn.mr-1(fab dark color='primary' @click='formerPage')
                  v-icon mdi-chevron-left
                v-btn.ml-1(fab dark color='primary' @click='nextPage')
                  v-icon mdi-chevron-right

            //- info button with ingredients
            //- browse section for all dishes on all days 
            //- -> filter out for day, location, food preference, allergies
            //- sort by rating
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "DiscoverDishes",
  data() {
    return {
      // TODO: rating to be implemented
      // suggested_dish_rating: null,
      itemsPerPageArray: [3, 6, 9],
      search: "",
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 3,
      sortBy: "",
      selectedCategories: [
        "Vegan",
        "Vegetarian",
        "Pork",
        "Beef",
        "Poultry",
        "Alcohol",
        "Fish",
      ],
      filters: {
        // date: {
        //   start_date: null,
        //   end_date: null
        // },
        // float - reformat response with parseFloat()
        affordable: false,
        // array of mensas
        mensa_name: null,
        // boolean
        main_dish: false,
        food_preferences: {
          Vegan: false,
          Vegetarian: false,
          Pork: false,
          Beef: false,
          Poultry: false,
          Alcohol: false,
          Fish: false,
        },
        additives: {
          Dyed: false,
          Preservatives: false,
          Antioxidants: false,
          "Flavor enhancers": false,
          Sulphurated: false,
          Blackened: false,
          Waxed: false,
          Phosphate: false,
          Sweeteners: false,
          "Phenylalanine source": false,
        },
        allergies: {
          Gluten: false,
          Spelt: false,
          Barles: false,
          Oats: false,
          Kamut: false,
          Rye: false,
          Wheat: false,
          Crustaceans: false,
          Egg: false,
          Fish: false,
          Peanuts: false,
          Soy: false,
          Milk: false,
          Nuts: false,
          Almonds: false,
          Hazelnuts: false,
          Walnuts: false,
          Cashews: false,
          Pecans: false,
          "Brazil nuts": false,
          Pistachios: false,
          Macadamias: false,
          Celerey: false,
          Mustard: false,
          Sesame: false,
          Lupines: false,
          Molluscs: false,
          "Sulfur dioxide": false,
        },
      },
    };
  },
  computed: {
    items: {
      get() {
        if (!this.$store.state.dishplan) return null;
        return this.$store.state.dishplan.filter(
          (dish) =>
            // filter by search term
            dish.dish.name.includes(this.search) &
            this.checkCategory(dish) &
            (this.filters.affordable
              ? this.$store.state.card_balance >= parseFloat(dish.priceStudent)
              : true) &
            (this.filters.main_dish ? dish.dish.main : true)
        );
      },
      set() {
        null;
      },
    },
    loaded() {
      if (this.items != null) return true;
      else return false;
    },
    numberOfPages() {
      if (this.items) return Math.ceil(this.items.length / this.itemsPerPage);
      else return 1;
    },
    filteredKeys() {
      return this.keys.filter((key) => key !== "Name");
    },
  },
  methods: {
    ...mapActions(["GetDishplan"]),

    checkCategory(dish) {
      if (dish.dish.categories != undefined) {
        for (let i = 0; i < dish.dish.categories.length; i++) {
          if (
            !this.selectedCategories.includes(
              dish.dish.categories[i].category.name
            )
          )
            return false;
        }
        // ! this.filters.food_preferences[dish.dish.categories[0].category.name]
      }
      return true;
      // this.filters.food_preferences[dish.dish.categories[0].category.name]
    },
    nextPage() {
      if (this.page + 1 <= this.numberOfPages) this.page += 1;
    },
    formerPage() {
      if (this.page - 1 >= 1) this.page -= 1;
    },
    updateItemsPerPage(number) {
      this.itemsPerPage = number;
    },
    getGoogleMapsUrl(mensaName) {
      const url = new URL("https://www.google.com/maps/dir/?api=1");
      url.searchParams.set("destination", mensaName);
      return url.toString();
    },
    async getDishplan() {
      try {
        await this.GetDishplan();
      } catch (error) {
        console.log(error);
      }
    },
    async getRecommendations() {
      try {
        var request_data = JSON.stringify({
          day: "2022.12.06",
          entire_week: "False",
        });
        await this.GetRecommendations(request_data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    // if items not set, query dishplan
    if (!this.items) this.getDishplan();
  },
};
</script>
