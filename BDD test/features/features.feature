Feature: Conversion d'image

  Scenario: Convertir PNG en JPEG
    Given I have an image "sample.png"
    When I convert the image to "JPEG" format
    Then the output should be a "JPEG" image

  Scenario: Redimensionner l'image et la convertir en JPEG
    Given I have an image "sample.png"
    When I convert the image to "JPEG" format with size 800x600
    Then the output should be a "JPEG" image
    And the output image should have size 800x600
