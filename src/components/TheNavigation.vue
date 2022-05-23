<template>
  <div class="NavBar">
    <div class="container">
      <router-link class="app-title" to="/">
        <svg
          width="32px"
          height="32px"
          viewBox="0 0 32 32"
          id="Layer_1"
          data-name="Layer 1"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M13,30H9a2.0027,2.0027,0,0,1-2-2V20H9v8h4V20h2v8A2.0027,2.0027,0,0,1,13,30Z"
            transform="translate(0 0)"
          />
          <polygon
            points="25 20 23.25 20 21 29.031 18.792 20 17 20 19.5 30 22.5 30 25 20"
          />
          <rect x="15" y="2" width="2" height="5" />
          <rect
            x="21.6675"
            y="6.8536"
            width="4.958"
            height="1.9998"
            transform="translate(1.5191 19.3744) rotate(-45)"
          />
          <rect x="25" y="15" width="5" height="2" />
          <rect x="2" y="15" width="5" height="2" />
          <rect
            x="6.8536"
            y="5.3745"
            width="1.9998"
            height="4.958"
            transform="translate(-3.253 7.8535) rotate(-45)"
          />
          <path
            d="M22,17H20V16a4,4,0,0,0-8,0v1H10V16a6,6,0,0,1,12,0Z"
            transform="translate(0 0)"
          />
          <rect
            id="_Transparent_Rectangle_"
            data-name="&lt;Transparent Rectangle&gt;"
            class="cls-1"
            width="32"
            height="32"
          />
        </svg>
        <span class="text">ARI</span>
      </router-link>
      <div class="content">
        <nav>
          <router-link class="links" to="/sponsor">Sponsors</router-link>
        </nav>
        <div class="icons">
          <div class="apperance">
            <button ref="toggle" @click="ToggleTheme">Switch mode</button>
          </div>
          <div class="social_links">
            <a href="http://github.com" title="github">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true"
                focusable="false"
                viewBox="0 0 24 24"
                class="vt-social-link-icon"
              >
                <path
                  d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
                ></path>
              </svg>
            </a>
            <a href="http://">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true"
                focusable="false"
                viewBox="0 0 24 24"
                class="vt-social-link-icon"
              >
                <path
                  d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
                ></path>
              </svg>
            </a>
            <a href="http://">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true"
                focusable="false"
                viewBox="0 0 24 24"
                class="vt-social-link-icon"
              >
                <path
                  d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
                ></path>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.NavBar {
  height: $nav-bar-height;
  padding: 0 32px;
  background: #f1f1f1;
  font-size: 13px;
  .links {
    color: var(--light-dark-text);
    margin: 13px;
  }
  .links:hover {
    cursor: pointer;
    color: $text-hover-green;
  }
  .container {
    @include flex(space-between, center);
    margin: 0 auto;
    max-width: 100%;
    .app-title {
      @include flex(center, center);
      width: $nav-bar-height;
      height: $nav-bar-height;
    }
    .content {
      @include flex(flex-end, center);
      flex-grow: 1;
      height: 100%;
      nav {
        @include flex(center, center);
        height: $nav-bar-height;
        flex-grow: 0.5;
      }
      .social_links {
        display: flex;
        flex-grow: 2;
        a {
          width: 30px;
          height: 30px;
          margin: 0 7px;
        }
      }
    }
  }
  .icons {
    display: flex;
    align-items: center;
  }
}
</style>
<script>
export default {
  methods: {},
};
</script>
