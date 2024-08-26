import re
from mkdocs.plugins import BasePlugin
import os

class BootstrapElementsPlugin(BasePlugin):

    def on_config(self, config):
        # Add CSS file
        css_file = os.path.join(os.path.dirname(__file__), 'css', 'bootstrap_elements.css')
        css_file = css_file.replace(os.sep, '/')  # Convert to forward slashes
        config['extra_css'] = config.get('extra_css', []) + [css_file]

        # Add JS file
        js_file = os.path.join(os.path.dirname(__file__), 'js', 'bootstrap_elements.js')
        js_file = js_file.replace(os.sep, '/')  # Convert to forward slashes
        config['extra_javascript'] = config.get('extra_javascript', []) + [js_file]

        return config

    def on_post_page(self, output_content, page, config):
        # Process accordions, modals, and cards
        output_content = self.process_accordions(output_content)
        output_content = self.process_modals(output_content)
        output_content = self.process_cards(output_content)
        
        # Add JavaScript for accordion and modal functionality
        custom_js = """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Accordion functionality
            document.querySelectorAll('.accordion-button').forEach(button => {
                button.addEventListener('click', () => {
                    const accordionContent = button.nextElementSibling;
                    if (accordionContent) {
                        button.classList.toggle('collapsed');
                        if (accordionContent.style.maxHeight) {
                            accordionContent.style.maxHeight = null;
                        } else {
                            accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
                        }
                    }
                });
            });

            // Modal functionality
            document.querySelectorAll('[data-bs-toggle="modal"]').forEach(button => {
                button.addEventListener('click', () => {
                    const targetId = button.getAttribute('data-bs-target');
                    const target = document.querySelector(targetId);
                    if (target) {
                        target.style.display = 'block';
                    }
                });
            });

            document.querySelectorAll('.modal .btn-close, .modal .btn-secondary').forEach(button => {
                button.addEventListener('click', () => {
                    const modal = button.closest('.modal');
                    if (modal) {
                        modal.style.display = 'none';
                    }
                });
            });

            // Close modal when clicking outside of it
            window.addEventListener('click', (event) => {
                if (event.target.classList.contains('modal')) {
                    event.target.style.display = 'none';
                }
            });
        });
        </script>
        """
        
        # Insert the JavaScript just before the closing </body> tag
        output_content = output_content.replace('</body>', f'{custom_js}</body>')
        
        return output_content

    def process_accordions(self, content):
        accordion_pattern = r':::accordion\s+(.*?)\n(.*?):::'
        accordion_id = 0
        
        def accordion_replace(match):
            nonlocal accordion_id
            title = match.group(1)
            content = match.group(2)
            accordion_id += 1
            return f'''
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading{accordion_id}">
                    <button class="accordion-button collapsed" type="button" aria-expanded="false" aria-controls="collapse{accordion_id}">
                        {title}
                    </button>
                </h2>
                <div id="collapse{accordion_id}" class="accordion-collapse collapse" aria-labelledby="heading{accordion_id}">
                    <div class="accordion-body">
                        {content}
                    </div>
                </div>
            </div>
            '''
        
        return re.sub(accordion_pattern, accordion_replace, content, flags=re.DOTALL)

    def process_modals(self, content):
        modal_pattern = r':::modal\s+(.*?)\n(.*?):::'
        modal_id = 0
        
        def modal_replace(match):
            nonlocal modal_id
            title = match.group(1)
            content = match.group(2)
            modal_id += 1
            return f'''
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{modal_id}">
              {title}
            </button>

            <div class="modal" id="modal{modal_id}" tabindex="-1" aria-labelledby="modalLabel{modal_id}" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modalLabel{modal_id}">{title}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    {content}
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
            '''
        
        return re.sub(modal_pattern, modal_replace, content, flags=re.DOTALL)

    def process_cards(self, content):
        card_pattern = r':::card\s+(.*?)\n(.*?):::'
        
        def card_replace(match):
            title = match.group(1)
            content = match.group(2)
            return f'''
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{title}</h5>
                <p class="card-text">{content}</p>
              </div>
            </div>
            '''
        
        return re.sub(card_pattern, card_replace, content, flags=re.DOTALL)